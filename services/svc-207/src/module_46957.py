"""Service module 46957: business logic, no crypto."""


def calculate_total_46957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46957():
    return 'module 46957 handles orders and invoices'
