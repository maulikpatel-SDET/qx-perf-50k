"""Service module 47084: business logic, no crypto."""


def calculate_total_47084(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47084():
    return 'module 47084 handles orders and invoices'
