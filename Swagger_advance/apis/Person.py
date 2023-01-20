
data = {"Dhanush":"M","Amrutha":"F","Yashodha":"F"}

from flask_restplus import Resource,Namespace

person = Namespace("person_t","Person details")

aru = person.parser()

aru.add_argument("name",type=str,help='Name of person to get there gender',required=True)

@person.route("/")
@person.doc(respones={200:'OK',400:"Data not there"})
@person.expect(aru)
class Person(Resource):
    global data
    def post(self):
        args = aru.parse_args()
        name = str.capitalize(args.get('name'))
        try:
            value = data[name]
            return {"Gender":value,"name":name},200
        except Exception as e:
            return {"message":"error"},400