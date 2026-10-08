"""Service module 34365: business logic, no crypto."""


def calculate_total_34365(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34365():
    return 'module 34365 handles orders and invoices'
