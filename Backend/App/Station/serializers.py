# App/Station/serializer.py
# import from framework
from rest_framework import serializers
# import from project
from .models import Station
from App.Combination.models import RouteXStation
from App.Combination.serializers import RouteXStationSerializer

# 用于显示站点
class ShowStation(serializers.ModelSerializer):
    station_id = serializers.IntegerField(required=False)
    routes = RouteXStationSerializer(source='routexstation_set', required=False, many=True)
    class Meta:
        model = Station
        fields = "__all__"

# 用于编辑站点
class EditStation(serializers.ModelSerializer):
    station_x_cor = serializers.IntegerField(required=False)
    station_y_cor = serializers.IntegerField(required=False)
    def create(self, data):
        station = Station.objects.create(station_id=Station.objects.count()+1, station_name=data["station_name"])
        # 由于外键约束无法直接插入数据库
        # route_x_station = RouteXStation.objects.create(station_id=station.id, seq=data, route_id=data["route_id"])
        # 不能在此使用route=Route.objects.get()会导致交叉引用
        try:
            combination = RouteXStationSerializer(data={"route": data["route_id"], "seq": data["seq"], "station": station.station_id})
            if combination.is_valid():
                combination.save()
            else:
                raise Exception("Failed to combine route & station")
        except KeyError:
            pass
        return station
    def update(self, instance, data):
        # 去掉原先的关联
        try:
            ex_relation = RouteXStation.objects.filter(route_id=data["route_id"], station_id=instance.station_id)
            if ex_relation:
                ex_relation.delete()
            new_combination = RouteXStationSerializer(data={"route":data.pop("route_id"), "seq": data.pop("seq"), "station": instance.station_id})
            if new_combination.is_valid():
                new_combination.save()
            else:
                raise Exception("Failed to combine route & station")
        except KeyError:
            pass
        for k in data:
            setattr(instance, k, data[k])
        instance.save()
        return instance
    def validate(self, data):
        if 'route_id' in self.context and 'seq' in self.context:
        # if get context = {"route_id", "seq"}
        # 查重 route_id -> seq
        # 用objects.get()而非objects.filter()
        # 因为objects.get()在找不到对象的时候抛出异常, 而objects.filter()仅仅返回一个空列表

        # RouteXStation & RouteXStationSerializer列名的对应关系
        # |     RouteXStation        | route_di | seq | station_id
        # | RouteXStationSerializer  | route    | seq | station
            route = RouteXStation.objects.filter(route_id=self.context["route_id"])
            if route:
                try:
                    route.get(seq=self.context["seq"])
                except RouteXStation.DoesNotExist:
                    data["route_id"] = self.context["route_id"]
                    data["seq"] = self.context["seq"]
                    return data
                else:
                    raise serializers.ValidationError("seq dumplicate")
            else:
                raise serializers.ValidationError("Route of route_id DOES NOT exist")                      
        else:
            return data
    class Meta:
        model = Station
        fields = ('station_name', 'station_x_cor', 'station_y_cor')