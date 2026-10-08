"""Service module 1957: business logic, no crypto."""


def calculate_total_1957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1957():
    return 'module 1957 handles orders and invoices'
