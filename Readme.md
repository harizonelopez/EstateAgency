# EstateAgency

EstateAgency is a real-estate agency application for discovering properties and contacting the agency about a listing. This README outlines the project's purpose, planned functionality, and practical guidance for development and maintenance.

## Project status

**In development.** The repository's implementation and configuration are the source of truth. Update this document as features and setup instructions are confirmed.

## Product scope

The application is intended to support:

- Browsing residential and commercial property listings.
- Viewing listing details, photographs, location, price, and availability.
- Finding listings with search and filters, such as location, sale or rental, property type, and price range.
- Sending an enquiry to the agency about a specific property.
- Viewing agency information and contact details.
- Using the experience on desktop, tablet, and mobile screens.

## Typical visitor workflow

1. Browse the available listings.
2. Refine the results using the available search controls.
3. Open a listing and review its details and current availability.
4. Submit an enquiry with contact information and a message.
5. The agency follows up using the details supplied.

## Property listing details

Where applicable, a listing should provide:

| Information | Guidance |
| --- | --- |
| Title and description | Clearly describe the property and its notable features. |
| Listing and property type | Identify sale or rental, and the kind of property. |
| Price | Include currency; for rentals, state the rental period. |
| Location | Show an appropriate public-facing address or area. |
| Attributes | Include relevant details such as bedrooms, bathrooms, and floor area. |
| Images | Use representative images and provide text alternatives. |
| Availability | Make it clear whether the property is currently available for enquiry. |

## Development and running the project

The framework, runtime, dependencies, and commands are not established in this README. Consult the repository's manifests and configuration before installing or running the application. Document verified commands here rather than assuming a particular technology stack.

When project setup is confirmed, add:

1. Supported runtime and tool versions.
2. Dependency installation instructions.
3. Required environment variables and a sanitized example configuration.
4. Local development and production build commands.
5. Test, lint, and formatting commands.

Never include real credentials, customer information, or production data in documentation or source control.

## Quality, accessibility, and privacy

- Validate enquiry data on the server and provide clear feedback for invalid submissions.
- Collect only information needed to respond to an enquiry and explain its intended use.
- Keep listing details, prices, and availability accurate; label sample content clearly.
- Ensure interactive controls work with a keyboard and have meaningful accessible names.
- Provide text alternatives for informative images and handle missing images gracefully.
- Design useful empty, loading, error, and unavailable-listing states.

## Contribution guidance

Keep changes focused and consistent with the existing codebase. Run the relevant checks available in the repository before submitting changes. Update this README when the setup process, supported functionality, or visitor workflows change.