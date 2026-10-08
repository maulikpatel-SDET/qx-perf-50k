"""Service module 8328: business logic, no crypto."""


def calculate_total_8328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8328():
    return 'module 8328 handles orders and invoices'
