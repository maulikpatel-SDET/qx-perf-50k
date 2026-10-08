"""Service module 44432: business logic, no crypto."""


def calculate_total_44432(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44432():
    return 'module 44432 handles orders and invoices'
