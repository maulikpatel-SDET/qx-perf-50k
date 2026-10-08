"""Service module 23579: business logic, no crypto."""


def calculate_total_23579(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23579():
    return 'module 23579 handles orders and invoices'
