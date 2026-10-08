"""Service module 43573: business logic, no crypto."""


def calculate_total_43573(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43573():
    return 'module 43573 handles orders and invoices'
