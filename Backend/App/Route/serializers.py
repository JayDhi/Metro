# App/Route/serializers.py
# import from framework
from rest_framework import serializers
# import from project
from .models import Route
from App.Combination.models import RouteXStation
from App.Combination.serializers import RouteXStationSerializer

# 用于显示站点
class ShowRoute(serializers.ModelSerializer):
    stations = RouteXStationSerializer(source='routexstation_set', required=False, many=True)
    class Meta:
        model = Route
        fields = ('route_name', 'route_id', 'stations')

# 用于编辑站点
# {"route":
#  "relationship": {
#       station1:{"station_name": , "seq":},
#       station2:{"station_name": , "seq":}}}
class EditRoute(serializers.ModelSerializer):
    def create(self, data):
        route = Route.objects.create(route_id=Route.objects.count()+1, route_name=data.pop("route_name"))
        for k in data:
            try:
                combination = RouteXStationSerializer(data={"route": route.route_id, "seq": data[k]["seq"], "station": data[k]["station_id"]})
                if combination.is_valid():
                    combination.save()
                else:
                    raise Exception("Failed to combine route & station")
            except KeyError:
                pass
        return route
    def update(self, instance, data):
        try:
            # 目前仅支持更改站点名称
            # 为了避免对附属站点的遍历过于麻烦，将data结构设计为{"route_id", "station_1", ...}
            # 而不是{"route_id", "stations":{"station1", ...}}
            # 而这种结构在遍历站点信息的时候应当保证字典是{"station1", ....}
            # 所以现将route_id取出保存在另一个变量中
            route_name = data.pop("route_name")
            instance.route_name = route_name
            for k in data:
                print(k)
                ex_relation = RouteXStation.objects.filter(route_id=instance.route_id, station_id=data[k]["station_id"])
                if ex_relation:
                    ex_relation.delete()
                new_relation = RouteXStationSerializer(data={"route": instance.route_id, "seq": data[k]["seq"], "station": data[k]["station_id"]})
                if new_relation.is_valid():
                    new_relation.save()
                    print(new_relation.data)
                else:
                    raise Exception("Failed to combine route & station")
        except Exception:
            raise Exception
        instance.save()
        return instance
    def validate(self, data):
        try:
            for k in self.context:
                print(k)
                station = RouteXStation.objects.filter(station_id=self.context[k]["station_id"])
                if station:
                    try:
                        station.get(seq=self.context[k]["seq"])
                    except RouteXStation.DoesNotExist:
                        pass
                    finally:
                        data[k] = {}
                        data[k]["station_id"] = self.context[k]["station_id"]
                        data[k]["seq"] = self.context[k]["seq"]
                else:
                    raise serializers.ValidationError("Station of station_id '%s' DOES NOT exist" % self.context[k]["station_id"])
            return data
        except KeyError:
            return data
    class Meta:
        model = Route
        fields = ('route_name',)