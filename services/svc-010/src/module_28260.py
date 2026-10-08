"""Service module 28260: business logic, no crypto."""


def calculate_total_28260(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28260():
    return 'module 28260 handles orders and invoices'
