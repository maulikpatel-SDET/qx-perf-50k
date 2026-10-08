"""Service module 3260: business logic, no crypto."""


def calculate_total_3260(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3260():
    return 'module 3260 handles orders and invoices'
