"""Service module 8186: business logic, no crypto."""


def calculate_total_8186(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8186():
    return 'module 8186 handles orders and invoices'
