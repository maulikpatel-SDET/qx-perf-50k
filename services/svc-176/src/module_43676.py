"""Service module 43676: business logic, no crypto."""


def calculate_total_43676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43676():
    return 'module 43676 handles orders and invoices'
