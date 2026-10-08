"""Service module 30129: business logic, no crypto."""


def calculate_total_30129(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30129():
    return 'module 30129 handles orders and invoices'
