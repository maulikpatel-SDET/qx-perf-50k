"""Service module 49356: business logic, no crypto."""


def calculate_total_49356(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49356():
    return 'module 49356 handles orders and invoices'
