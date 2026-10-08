"""Service module 33669: business logic, no crypto."""


def calculate_total_33669(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33669():
    return 'module 33669 handles orders and invoices'
