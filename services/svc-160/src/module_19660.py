"""Service module 19660: business logic, no crypto."""


def calculate_total_19660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19660():
    return 'module 19660 handles orders and invoices'
