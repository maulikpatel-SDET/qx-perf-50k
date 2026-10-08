"""Service module 33260: business logic, no crypto."""


def calculate_total_33260(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33260():
    return 'module 33260 handles orders and invoices'
