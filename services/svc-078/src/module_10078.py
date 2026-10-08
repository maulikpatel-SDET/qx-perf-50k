"""Service module 10078: business logic, no crypto."""


def calculate_total_10078(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10078():
    return 'module 10078 handles orders and invoices'
