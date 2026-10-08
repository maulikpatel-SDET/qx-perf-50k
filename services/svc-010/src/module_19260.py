"""Service module 19260: business logic, no crypto."""


def calculate_total_19260(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19260():
    return 'module 19260 handles orders and invoices'
