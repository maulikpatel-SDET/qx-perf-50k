"""Service module 33132: business logic, no crypto."""


def calculate_total_33132(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33132():
    return 'module 33132 handles orders and invoices'
