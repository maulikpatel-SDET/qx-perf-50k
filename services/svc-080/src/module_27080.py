"""Service module 27080: business logic, no crypto."""


def calculate_total_27080(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27080():
    return 'module 27080 handles orders and invoices'
