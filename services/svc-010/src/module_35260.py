"""Service module 35260: business logic, no crypto."""


def calculate_total_35260(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35260():
    return 'module 35260 handles orders and invoices'
