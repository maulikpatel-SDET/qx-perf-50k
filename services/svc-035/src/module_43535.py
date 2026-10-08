"""Service module 43535: business logic, no crypto."""


def calculate_total_43535(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43535():
    return 'module 43535 handles orders and invoices'
