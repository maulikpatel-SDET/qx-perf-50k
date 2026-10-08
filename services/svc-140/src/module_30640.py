"""Service module 30640: business logic, no crypto."""


def calculate_total_30640(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30640():
    return 'module 30640 handles orders and invoices'
