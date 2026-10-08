"""Service module 34221: business logic, no crypto."""


def calculate_total_34221(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34221():
    return 'module 34221 handles orders and invoices'
