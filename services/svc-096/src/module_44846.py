"""Service module 44846: business logic, no crypto."""


def calculate_total_44846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44846():
    return 'module 44846 handles orders and invoices'
