class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        # Write code here
        end.next=data
        data.prev=end
        end=data
        data.next=head.prev
        head.prev=end
        

    def add_at_head(self, data) -> bool:
        # Write code here
        head.prev=data
        data.next=head
        head=data
        data.prev=end.next
        end.next=head

    def add_at_index(self, index, data) -> bool:
        # Write code here
        data.next=index
        data.prev=index.prev
        data.prev.next=data
        index.prev=data

    def get(self, index) -> int:
        # Write code here
        return index

    def delete_at_index(self, index) -> bool:
        # Write code here
        if index.prev==NULL:
            head=index.next
            head.prev=end.next
        elif index.next==NULL:
            end=index.prev
            end.next=NULL
        else:
            index.prev.next=index.next
            index.next.prev=index.prev
        delete(n)

    def get_previous_next(self, index) -> list:
        # Write code here
        return index.prev
        return index.next
    


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
