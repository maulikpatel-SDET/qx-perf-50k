"""Service module 46600: business logic, no crypto."""


def calculate_total_46600(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46600():
    return 'module 46600 handles orders and invoices'
