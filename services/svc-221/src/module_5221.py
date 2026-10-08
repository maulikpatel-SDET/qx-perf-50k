"""Service module 5221: business logic, no crypto."""


def calculate_total_5221(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5221():
    return 'module 5221 handles orders and invoices'
