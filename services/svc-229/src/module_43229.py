"""Service module 43229: business logic, no crypto."""


def calculate_total_43229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43229():
    return 'module 43229 handles orders and invoices'
