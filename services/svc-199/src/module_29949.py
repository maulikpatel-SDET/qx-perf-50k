"""Service module 29949: business logic, no crypto."""


def calculate_total_29949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29949():
    return 'module 29949 handles orders and invoices'
