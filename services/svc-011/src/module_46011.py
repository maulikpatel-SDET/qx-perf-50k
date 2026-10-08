"""Service module 46011: business logic, no crypto."""


def calculate_total_46011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46011():
    return 'module 46011 handles orders and invoices'
