"""Service module 23328: business logic, no crypto."""


def calculate_total_23328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23328():
    return 'module 23328 handles orders and invoices'
