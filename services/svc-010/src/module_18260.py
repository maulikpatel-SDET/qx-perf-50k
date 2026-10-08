"""Service module 18260: business logic, no crypto."""


def calculate_total_18260(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18260():
    return 'module 18260 handles orders and invoices'
