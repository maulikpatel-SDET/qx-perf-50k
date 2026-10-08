"""Service module 18324: business logic, no crypto."""


def calculate_total_18324(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18324():
    return 'module 18324 handles orders and invoices'
