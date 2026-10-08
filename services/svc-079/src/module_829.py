"""Service module 829: business logic, no crypto."""


def calculate_total_829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_829():
    return 'module 829 handles orders and invoices'
