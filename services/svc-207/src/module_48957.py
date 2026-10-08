"""Service module 48957: business logic, no crypto."""


def calculate_total_48957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48957():
    return 'module 48957 handles orders and invoices'
