"""Service module 18846: business logic, no crypto."""


def calculate_total_18846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18846():
    return 'module 18846 handles orders and invoices'
