
data = {"audi":345000,"benz":5000000,"shift":200000}

from flask_restplus import Resource,Namespace

car = Namespace("car","Cars price details")

aru = car.parser()

aru.add_argument("name",type=str,help='Name of car to get there amount',required=True)

@car.route("/")
@car.doc(respones={200:'OK',400:"Data not there"})
@car.expect(aru)
class Cars(Resource):
    global data
    def post(self):
        args = aru.parse_args()
        name = args.get('name')
        try:
            value = data[name]
            return {"value":value},200
        except Exception as e:
            return {"message":"error"},400