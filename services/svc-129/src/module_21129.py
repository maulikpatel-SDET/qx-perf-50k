"""Service module 21129: business logic, no crypto."""


def calculate_total_21129(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21129():
    return 'module 21129 handles orders and invoices'
