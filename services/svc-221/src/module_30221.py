"""Service module 30221: business logic, no crypto."""


def calculate_total_30221(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30221():
    return 'module 30221 handles orders and invoices'
