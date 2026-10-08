"""Service module 33277: business logic, no crypto."""


def calculate_total_33277(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33277():
    return 'module 33277 handles orders and invoices'
