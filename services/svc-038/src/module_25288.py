"""Service module 25288: business logic, no crypto."""


def calculate_total_25288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25288():
    return 'module 25288 handles orders and invoices'
