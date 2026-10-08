"""Service module 36086: business logic, no crypto."""


def calculate_total_36086(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36086():
    return 'module 36086 handles orders and invoices'
