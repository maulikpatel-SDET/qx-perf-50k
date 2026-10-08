"""Service module 36795: business logic, no crypto."""


def calculate_total_36795(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36795():
    return 'module 36795 handles orders and invoices'
