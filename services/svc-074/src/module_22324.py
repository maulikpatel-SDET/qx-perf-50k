"""Service module 22324: business logic, no crypto."""


def calculate_total_22324(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22324():
    return 'module 22324 handles orders and invoices'
