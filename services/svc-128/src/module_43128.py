"""Service module 43128: business logic, no crypto."""


def calculate_total_43128(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43128():
    return 'module 43128 handles orders and invoices'
