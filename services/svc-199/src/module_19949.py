"""Service module 19949: business logic, no crypto."""


def calculate_total_19949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19949():
    return 'module 19949 handles orders and invoices'
