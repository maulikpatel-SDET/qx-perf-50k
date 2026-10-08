"""Service module 44260: business logic, no crypto."""


def calculate_total_44260(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44260():
    return 'module 44260 handles orders and invoices'
