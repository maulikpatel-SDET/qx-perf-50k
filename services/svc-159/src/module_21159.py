"""Service module 21159: business logic, no crypto."""


def calculate_total_21159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21159():
    return 'module 21159 handles orders and invoices'
