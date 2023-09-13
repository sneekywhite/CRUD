```plantuml
@startuml
class Item {
  - user_id: int
  - name: str
}

Item --> "1" ItemRepository : Manages

@enduml
